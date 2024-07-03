
// 文字サイズチェンジ
$(function() {
    function changeFontSize(buttonID, className) {
        $('body').removeClass('f-small f-large');
        $('body').addClass(className);
        $('.current').removeClass('current');
        $(buttonID).addClass('current');
    }

    // 初期設定。ここを'#f-large'と'f-large'に変更すれば、デフォルトが大文字になります。
    changeFontSize('#f-small', 'f-small');

    $('#f-small').click(function() {
        changeFontSize('#f-small', 'f-small');
    });

    $('#f-large').click(function() {
        changeFontSize('#f-large', 'f-large');
    });
});
