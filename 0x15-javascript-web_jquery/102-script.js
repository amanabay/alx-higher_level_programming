$(function () {
  $('INPUT#btn_translate').click(function () {
    const languageCode = $('INPUT#language_code').val();
    const apiUrl = 'https://www.fourtonfish.com/hellosalut/hello/';
    $.ajax({
      url: apiUrl + languageCode,
      type: 'GET',
      success: function (data) {
        $('DIV#hello').text(data.hello);
      }
    });
  });
});
