from fastapi import FastAPI

from msaUtils.profiler import MSAProfilerMiddleware
from msaUtils.scheduler import MSAScheduler
from msaUtils.sysinfo import MSASystemInfo, get_sysinfo

app = FastAPI()

...

# sysinfo
sysinfo: MSASystemInfo = get_sysinfo()
# return app.templates.TemplateResponse(
#     "monitor.html", {"request": request, "outputSystemInfo": sysinfo}
# )

# profiler middleware
app.add_middleware(
    MSAProfilerMiddleware
)


# scheduler
async def test_timer_min():
    print("msaSDK Test Timer Async Every Minute")


def test_timer_five_sec():
    print("msaSDK Test Timer Sync 5 Second")


myScheduler = MSAScheduler()
myScheduler.task("every 1 min", func=test_timer_min)
myScheduler.task("every 5 sec", func=test_timer_five_sec)