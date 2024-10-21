// /** @odoo-module */

import { registerMessagingComponent } from '@mail/utils/messaging_component';
import { replace } from '@mail/model/model_field_command';
import { FileUploader } from '@mail/components/file_uploader/file_uploader';
import { patch } from 'web.utils';
import Dialog from 'web.Dialog';
import core from 'web.core';


const { Component } = owl;
const { useRef } = owl.hooks;

const geAttachmentNextTemporaryId = (function () {
    let tmpId = 0;
    return () => {
        tmpId -= 1;
        return tmpId;
    };
})();


patch(FileUploader.prototype, 'calendar/static/src/components/file_uploader/file_uploader.js', {
    /**
     * @private
     * @param {Object} param0
     * @param {mail.composer} param0.composer
     * @param {FileList|Array} param0.files
     * @param {mail.thread} param0.thread
     * @returns {Promise}
     */
    async _performUpload({ composer, files, thread }) {
        var Dialog = require('web.Dialog');
        const uploadingAttachments = new Map();

        for (const file of files) {
            if (file.size>2000000){
                var file_name = file.name
                var file_Size= file.size

                file_Size = Math.round(file_Size/1000000) 
                var c = "The size of file \n" + file_name +" is = " + file_Size +"MB, \n which is more than our requested size. The maximum size sent should be 5MB."
                Dialog.alert(this,c,{
                        onForceClose: function(){
                            return;
                        },
                        confirm_callback: function(){
                            return;
                        }
                    }
                 );
                 continue;
            }
            uploadingAttachments.set(file, this.messaging.models['mail.attachment'].insert({
                composer: composer && replace(composer),
                filename: file.name,
                id: geAttachmentNextTemporaryId(),
                isUploading: true,
                mimetype: file.type,
                name: file.name,
                originThread: (!composer && thread) ? replace(thread) : undefined,
            }));
        }
        for (const file of files) {
            if (file.size>2000000){
                continue;
            }
            const uploadingAttachment = uploadingAttachments.get(file);
            if (!uploadingAttachment.exists()) {
                // This happens when a pending attachment is being deleted by user before upload.
                continue;
            }
            if ((composer && !composer.exists()) || (thread && !thread.exists())) {
                return;
            }
            try {
                const response = await this.env.browser.fetch('/mail/attachment/upload', {
                    method: 'POST',
                    body: this._createFormData({ composer, file, thread }),
                    signal: uploadingAttachment.uploadingAbortController.signal,
                });
                const attachmentData = await response.json();
                if (uploadingAttachment.exists()) {
                    uploadingAttachment.delete();
                }
                if ((composer && !composer.exists()) || (thread && !thread.exists())) {
                    return;
                }
                this._onAttachmentUploaded({ attachmentData, composer, thread });
            } catch (e) {
                if (e.name !== 'AbortError') {
                    throw e;
                }
            }
        }        
    }
});
