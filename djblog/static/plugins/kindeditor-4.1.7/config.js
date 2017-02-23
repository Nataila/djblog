KindEditor.ready(function(K) {
    window.editor = K.create('#id_content',{
        // 指定大小
        width:'800px',
        height:'1000px',
        // uploadJson: '/post_upload_image/',
        // cssPath: 'plugins/code/prettify.css',
        // extraFileUploadParams: {
        //   csrfmiddlewaretoken: $.cookie('csrftoken')
        // }
    });
});
