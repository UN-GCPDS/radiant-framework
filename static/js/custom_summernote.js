document.addEventListener("load", function(){

$('#summernote').summernote({
  styleTags: [
    'p',
        { title: 'Blockquote', tag: 'blockquote', className: 'blockquote', value: 'blockquote' },
        'pre', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'
    ],


  });

});
