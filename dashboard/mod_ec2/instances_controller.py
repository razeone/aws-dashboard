import boto3
from botocore.exceptions import ClientError
import logging


class InstancesController:

    def __init__(self):
        self.__set_ec2_resource()
        self.__set_ec2_client()

    def __set_ec2_client(self):
        try:
            self.client = boto3.client('ec2')
        except ClientError as e:
            logging.error(e.response['Error']['Code'])

    def __set_ec2_resource(self):
        try:
            self.resource = boto3.resource('ec2')
        except ClientError as e:
            logging.error(e.response['Error']['Code'])

    def check_health_status(self):
        try:
            logging.info("Checking status")
            return self.client.describe_instance_status()['InstanceStatuses']
        except ClientError as e:
            logging.error(e.response['Error']['Code'])

    def describe_instances(self):
        try:
            logging.info("Describing instances")
            return self.client.describe_instances()
        except ClientError as e:
            logging.error(e.response['Error']['Code'])

    def get_running_instances(self):
        try:
            logging.info("Get running instances")
            return self.resource.instances.filter(
                Filters=[{'Name': 'instance-state-name',
                          'Values': ['running']}])
        except ClientError as e:
            logging.error(e.response['Error']['Code'])

    def get_instance_obj(self, instance_id):
        try:
            logging.info("Getting instance object for " + instance_id)
            return self.resource.Instance(instance_id)
        except ClientError as e:
            logging.error(e.response['Error']['Code'])

    def stop_instance(self, instance_id):
        try:
            logging.info("Stopping instance " + instance_id)
            instance = self.get_instance_obj(instance_id)
            return instance.stop()
        except ClientError as e:
            logging.error(e.response['Error']['Code'])

    def start_instance(self, instance_id):
        try:
            logging.info("Starting instance " + instance_id)
            instance = self.get_instance_obj(instance_id)
            return instance.start()
        except ClientError as e:
            logging.error(e.response['Error']['Code'])

    def terminate_instace(self, instance_id):
        try:
            logging.info("Terminating instance " + instance_id)
            instance = self.get_instance_obj(instance_id)
            return instance.terminate()
        except ClientError as e:
            logging.error(e.response['Error']['Code'])

    def reboot_instance(self, instance_id):
        try:
            logging.info("Rebooting instance " + instance_id)
            instance = self.get_instance_obj(instance_id)
            return instance.reboot()
        except ClientError as e:
            logging.error(e.response['Error']['Code'])

    def reload_instance(self, instance_id):
        try:
            logging.info("Reloading instance " + instance_id)
            instance = self.get_instance_obj(instance_id)
            return instance.reload()
        except ClientError as e:
            logging.error(e.response['Error']['Code'])
