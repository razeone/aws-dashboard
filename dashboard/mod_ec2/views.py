from flask import Blueprint
from flask import render_template
from flask import abort
from jinja2 import TemplateNotFound
import boto3


mod_ec2 = Blueprint('mod_ec2', __name__,
                    template_folder='templates',
                    url_prefix='/ec2')


@mod_ec2.route('/', defaults={'page': 'ec2_menu'})
@mod_ec2.route('/<page>')
def show(page):
    """
    Shows the main page with all the reserved instances and a small description
    """
    try:
        return render_template('%s.html' % page)
    except TemplateNotFound:
        abort(404)


@mod_ec2.route('/describe_instances')
def describe_instances():
    try:
        ec2 = boto3.client('ec2')
        instances = ec2.describe_instances()
        return render_template('ec2_describe_instances.html',
                               instances=instances)
    except TemplateNotFound:
        abort(404)


@mod_ec2.route('/running_instances')
def running_instances():
    try:
        ec2 = boto3.resource('ec2')
        instances = ec2.instances.filter(
            Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
        return render_template('ec2_running_instances.html',
                               instances=instances)
    except TemplateNotFound:
        abort(404)
