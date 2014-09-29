from util.log import Log

class StreamHandler(object):
    
    reference_count = 0
    
    def __init__(self):
        self.streaming = False
    
    def subscribe_to_stream(self):
        StreamHandler.reference_count += 1
        if not self.streaming:
            self._start_streaming()

        return "StreamHandler#subscribe_to_stream"

    def unsubscribe_to_stream(self):
        StreamHandler.reference_count -= 1
        if StreamHandler.reference_count == 0:
            self._stop_streaming()
    
    def _start_streaming(self):
        self.streaming = True

    def _stop_streaming(self):
        self.streaming = False
        

class RtspStreamHandler(StreamHandler):

    
    def __init__(self):
        super(RtspStreamHandler, self).__init__()

        
    def subscribe_to_stream(self):
        super(RtspStreamHandler, self).subscribe_to_stream()
        url = "RtspStreamHandler#subscribe_to_stream"
        Log.info("Subscribing to RTSP stream")
        return url

    
    def unsubscribe_to_stream(self):
        super(RtspStreamHandler, self).unsubscribe_to_stream()
        Log.info("Unsubscribing to RTSP stream")
    

    def _start_streaming(self):
        super(RtspStreamHandler, self)._start_streaming()
        Log.info("Starting RTSP stream")


    def _stop_streaming(self):
        super(RtspStreamHandler, self)._stop_streaming()
        Log.info("Stopping RTSP stream")
    