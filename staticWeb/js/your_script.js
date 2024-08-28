(function($){
    $(document).ready(function(){
        $('form#changelist-form button[name="action"]').on('click', function(event){
            var selectedAction = $('select[name="action"]').val();
            if(selectedAction === 'your_action'){
                event.preventDefault();
                $.ajax({
                    url: window.location.href,
                    method: 'POST',
                    data: $('form#changelist-form').serialize(),
                    success: function(data){
                        if(data.status === 'success'){
                            alert(data.message);
                        }
                    }
                });
            }
        });
    });
})(django.jQuery);
