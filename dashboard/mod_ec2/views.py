from flask import Blueprint
from flask import render_template
from flask import abort
from flask import jsonify
from flask import request
from jinja2 import TemplateNotFound
from .instances_controller import InstancesController


mod_ec2 = Blueprint('mod_ec2', __name__,
                    template_folder='templates',
                    url_prefix='/ec2')


@mod_ec2.route('/', defaults={'page': 'ec2_home'})
@mod_ec2.route('/<page>')
def show(page):
    """
    Shows the main page with running and described instances
    """
    try:
        ic = InstancesController()
        running_instances = list(ic.get_running_instances())
        described_instances = ic.describe_instances()
        return render_template(
            '%s.html' % page,
            running_instances=running_instances,
            described_instances=described_instances['Reservations'])
    except TemplateNotFound:
        abort(404)


@mod_ec2.route('/describe_instances')
def describe_instances():
    """
    "Describe" all the allocated instances
    """
    try:
        ic = InstancesController()
        instances = ic.describe_instances()
        return render_template('ec2_describe_instances.html',
                               reservations=instances['Reservations'])
    except TemplateNotFound:
        abort(404)


@mod_ec2.route('/running_instances')
def running_instances():
    """
    Shows all the running instances
    """
    try:
        ic = InstancesController()
        instances = ic.get_running_instances()
        return render_template('ec2_running_instances.html',
                               instances=instances)
    except TemplateNotFound:
        abort(404)


@mod_ec2.route('/instances/<instance_id>')
def instance_dettail(instance_id):
    """
    Gets all the dettails for a given instance
    """
    try:
        ic = InstancesController()
        instance = ic.get_instance_obj(instance_id)
        return render_template('ec2_instance_dettail.html', instance=instance)
    except TemplateNotFound:
        abort(404)


@mod_ec2.route('/stop_instance', methods=["POST"])
def stop_instance():
    """
    Stops a running instance
    """
    try:
        params = request.json
    except Exception:
        return jsonify(error=400, text="Params are required"), 400
    try:
        if 'instance_id' in params:
            try:
                ic = InstancesController()
                result = ic.stop_instance(params['instance_id'])
                return jsonify(result), 200
            except Exception:
                abort(500)
        else:
            return jsonify(error=400, text="Instance id is required"), 400
        # ic = InstancesController()
        # result = ic.stop_instance(instance_id)
        # return result
    except TemplateNotFound:
        abort(404)


@mod_ec2.route('/start_instance', methods=["POST"])
def start_instance():
    """
    Starts a running instance
    """
    try:
        params = request.json
    except Exception:
        return jsonify(error=400, text="Params are required"), 400
    try:
        if 'instance_id' in params:
            try:
                ic = InstancesController()
                result = ic.start_instance(params['instance_id'])
                return jsonify(result), 200
            except Exception:
                abort(500)
        else:
            return jsonify(error=400, text="Instance id is required"), 400
        # ic = InstancesController()
        # result = ic.stop_instance(instance_id)
        # return result
    except TemplateNotFound:
        abort(404)
