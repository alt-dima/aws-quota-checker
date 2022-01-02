from .quota_check import QuotaCheck, QuotaScope, InstanceQuotaCheck


class BucketCountCheck(QuotaCheck):
    key = "s3_bucket_count"
    description = "S3 Buckets per account"
    scope = QuotaScope.REGION
    service_code = 's3'
    quota_code = 'L-DC2B2D3D'

    @property
    def current(self):
        return len(self.boto_session.client('s3').list_buckets()['Buckets'])
    
    #Answer from AWS support:unfortunately at this moment in time there is no way for you to check this limit from your side.
    @property
    def maximum(self):
        return int(-1)
