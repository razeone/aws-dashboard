from flask import Blueprint
from flask import render_template
from flask import abort
from jinja2 import TemplateNotFound
import boto3


mod_ec2 = Blueprint('mod_ec2', __name__,
                    template_folder='templates',
                    url_prefix='/ec2')


@mod_ec2.route('/', defaults={'page': 'ec2_home'})
@mod_ec2.route('/<page>')
def show(page):
    """
    Shows the main page with all the options for the menu
    """
    try:
        return render_template('%s.html' % page)
    except TemplateNotFound:
        abort(404)


@mod_ec2.route('/describe_instances')
def describe_instances():
    """
    "Describe" all the allocated instances
    """
    try:
        ec2 = boto3.client('ec2')
        instances = ec2.describe_instances()
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
        ec2 = boto3.resource('ec2')
        instances = ec2.instances.filter(
            Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
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
        ec2 = boto3.resource('ec2')
        instance = ec2.Instance(instance_id)
        return render_template('ec2_instance_dettail.html', instance=instance)
    except TemplateNotFound:
        abort(404)
