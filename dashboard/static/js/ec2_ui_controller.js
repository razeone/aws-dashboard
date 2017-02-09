$(function(){

	runningElements = $('.state-running').addClass('badge-success');
	stoppedElements = $('.state-stopped').addClass('badge-danger');
	pendingElements = $('.state-pending').addClass('badge-warning');
	stoppingElements = $('.state-stopping').addClass('badge-warning');

	function start_instance(instance_id){
		$.ajax({
			url: "/ec2/start_instance",
			method: "POST",
			data: {
				"instance_id": instance_id
			}
		}).done(function(data){
			alert(data);
		});
	}

});