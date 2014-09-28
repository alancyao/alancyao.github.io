$(window).load(function() {    

    var theWindow        = $(window),
      $bg              = $("#bg"),
      aspectRatio      = $bg.width() / $bg.height();
                    
  function resizeBg() {
        
        if ( (theWindow.width() / theWindow.height()) < aspectRatio ) {
                  $bg
            .removeClass()
            .addClass('bgwidth');
    } else {
              $bg
            .removeClass()
            .addClass('bgheight');
    }
                  
          }
                            
    theWindow.resize(resizeBg).trigger("resize");

});

