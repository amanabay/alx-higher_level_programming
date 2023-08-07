$(function () {
  $('INPUT#btn_translate').click(translation);
  $('INPUT#language_code').keypress(function (event) {
    if (event.which === 13) {
      translation();
    }
  });

  function translation () {
    const languageCode = $('INPUT#language_code').val();
    const apiUrl = 'https://www.fourtonfish.com/hellosalut/hello/';

    $.ajax({
      url: apiUrl + languageCode,
      type: 'GET',
      success: function (data) {
        $('DIV#hello').text(data.hello);
      }
    });
  }
});
