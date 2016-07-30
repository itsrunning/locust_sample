# locust_sample
A sample framework with Locust (a python based perf testing tool)

# The good
* Simple to configure.
* Minimalistic coding.
* Can be run distributedly (using master-slaves) - Not tried yet.
* Good web interface.

# Issues
* Limiting the execution time is not possible. By default Locust runs indefinitely. The only way to stop execution is to specify the maximum number of requests or manually stopping the run.
* Rampup cannot be controlled much. The only option is to specify the number of users/second.
* Requests that involve redirects are only reported as a group. Only the total time of all redirects is mentioned. The split of each redirect is not logged.
* Reporting seems to be a major issue. The count of requests (and possibly marking times against the wrong request) fired vs reported is unreliable.
* The order in which the requests are fired is not controllable and is random even if we list them in order.
* Not suitable for workflows that describe a specific user behavior.
