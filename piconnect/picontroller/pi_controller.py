from picontroller.streams.stream_handler import RtspStreamHandler

class PiController(object):
    '''
    A controller for the Raspberry Pi
    '''

    def __init__(self):
        self.stream_handler = RtspStreamHandler()
    
    def subscribe_to_rtsp_stream(self):
        """
        subscribes to rtsp stream, returns the stream url.
        """
        return self.stream_handler.subscribe_to_stream()
    
    def unsubscribe_to_rtsp_stream(self):
        """
        unsubscribes to rtsp stream.
        """
        self.stream_handler.unsubscribe_to_stream()
    
    