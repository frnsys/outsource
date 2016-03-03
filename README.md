`outsource` makes it easy to bid on and use AWS Spot Instances, which provide short-term computing power at a much cheaper rate.

Specify your AWS credentials in `~/.aws/credentials`:

    [default]
    aws_access_key_id = YOURACCESSKEY
    aws_secret_access_key = YOURSECRETKEY

    [another_profile]
    aws_access_key_id = YOURACCESSKEY
    aws_secret_access_key = YOURSECRETKEY

Then create a config at `config.yaml` with the following (filled with whatever values you prefer, of course):

    region: us-east-1
    profile: another_profile
    ami: ami-a0c499c8
    key_name: my_key_pair

If it will be consistent across your usage.

Then you have a few options:

    # Create a spot instance request
    $ outsource request <name> <instance type> [--user_data=<path to user data script>] [--ami=<image id>]
    $ outsource request doc2vec r3.2xlarge --user_data=user_data.sh
    # Then you can do:
    $ ssh -i my_key_pair.pem ubuntu@<instance's public ip>
    # Try `ec2-user` if `ubuntu` doesn't work

    # Cancel a spot instance request
    $ outsource cancel <request id>
    $ outsource cancel sir-02baen2k

    # Terminate a spot instance
    $ outsource terminate <name>
    $ outsource terminate doc2vec

    # List spot instances and requests
    $ outsource ls

You can refer to the `examples` folder for some example `user_data` scripts.

What `outsource` does for you:
- it will look at current bids for your requests instance type in your region, list out their min/max/mean, and suggest a bid price.
- it will create a security group with SSH access for your local machine (i.e. the machine making the spot instance request). It will also clean up this security group when you terminate the instance.
- it will tell you the public IP of the spot instance when it's ready.

Reference:

- Ubuntu AMIs: <https://cloud-images.ubuntu.com/releases/>
- Spot instance types: <https://aws.amazon.com/ec2/purchasing-options/spot-instances/>
- If your user data script doesn't seem to be executing...
    - check that your script is at `/var/lib/cloud/instance/scripts/part-001`
    - check the logs at `/var/log/cloud-init.log`
    - check the logs at `/var/log/cloud-init-output.log`
