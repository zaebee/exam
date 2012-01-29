$.ajaxSetup({
  beforeSend: function (request) {
      request.setRequestHeader('X-CSRFToken',getCookie('csrftoken'));
  },
});

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$(document).ready(function () {

	function activateTab($tab) {
		var $activeTab = $tab.closest('dl').find('a.active'),
				//contentLocation = $tab.attr("href") + 'Tab';
				contentLocation = $tab.attr("href");
        $.post(contentLocation, function(data){
        });

		//Make Tab Active
		$activeTab.removeClass('active');
		$tab.addClass('active');

    	//Show Tab Content
		//$(contentLocation).closest('.tabs-content').children('li').hide();
		//$(contentLocation).show();
	}

	$('dl.tabs').each(function () {
		//Get all tabs
		var tabs = $(this).children('dd').children('a');
		tabs.click(function (e) {
			activateTab($(this));
      return false;
		});
	});

	if (window.location.hash) {
		activateTab($('a[href="' + window.location.hash + '"]'));
	}

});
