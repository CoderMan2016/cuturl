function typed_init(){
  var typed2 = new Typed('#typed', {
    strings: ['Введите URL... ^1000', 'Сократите ссылку... ^1000', 'Поделитесь её... ^3000'],
    typeSpeed: 50,
    backSpeed: 20,
    fadeOut: true,
    loop: true
  });
}

typed_init()

$(".nav-sticky").sticky({topSpacing:0});

AOS.init();

function show_notification(){
  notification = $('.notification')

  notification.removeClass('hidden');
  notification.removeClass('fadeOut');
  notification.addClass('fadeIn');

  setTimeout(function(){
    notification.removeClass('fadeIn');
    notification.addClass('fadeOut');
  }, 2000)

}

function cut_link(){
  $('#cut_url__button').text('Сжимаю...')
  $.ajax({
    url: '/',
    type: 'POST',
    data: {
      'link': $('#cu__input').val()
    },
    success: function(responce){
      $('#main__section__wrapper').html(responce)
      $('#typed').text('Ваша ссылка готова')
      AOS.init();
      var clipboard = new ClipboardJS('.btn-clipboard');
    },
    error: function(responce){
      console.log(2);
    }
  })
}

function reset() {
  $.ajax({
    url: '/',
    type: 'POST',
    data: {
      'reset': true
    },
    success: function(data){
      $('#main__section__wrapper').html(data)
      typed_init()
      AOS.init();
    },
    error: function(responce){
      console.log(2);
    }
  })
}
