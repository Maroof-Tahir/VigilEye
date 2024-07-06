from inference import InferencePipeline

from inference.core.interfaces.stream.sinks import render_boxes


pipeline = InferencePipeline.init(
model_id="cds-gc5yj/4",
api_key="rOHmhOAmDW8U4OSb21Vy",
video_reference=0, # Path to video, device id (int, usually 0 for built in webcams), or RTSP stream url
on_prediction=render_boxes
)
pipeline.start()
pipeline.join()