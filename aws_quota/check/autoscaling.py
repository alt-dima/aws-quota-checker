from .quota_check import QuotaCheck, QuotaScope


class AutoScalingGroupCountCheck(QuotaCheck):
    key = "asg_count"
    description = "Auto Scaling groups per region"
    scope = QuotaScope.REGION
    service_code = 'autoscaling'
    quota_code = 'L-CDE20ADC'

    @property
    def current(self):
        return len(self.boto_session.client('autoscaling').describe_auto_scaling_groups()['AutoScalingGroups'])

class AutoScalingECSTargetsCountCheck(QuotaCheck):
    key = "ecsstrg_count"
    description = "ECS scalable targets per region"
    scope = QuotaScope.REGION
    service_code = 'application-autoscaling'
    quota_code = 'L-782A3EE2'

    @property
    def current(self):
        return len(self.boto_session.client('application-autoscaling').describe_scalable_targets(ServiceNamespace='ecs',)['ScalableTargets'])


class LaunchConfigurationCountCheck(QuotaCheck):
    key = "lc_count"
    description = "Launch configurations per region"
    scope = QuotaScope.REGION
    service_code = 'autoscaling'
    quota_code = 'L-6B80B8FA'

    @property
    def current(self):
        return len(self.boto_session.client('autoscaling').describe_launch_configurations()['LaunchConfigurations'])
