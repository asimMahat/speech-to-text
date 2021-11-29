import React from "react";
import "../App.css";
import { useReactMediaRecorder } from "react-media-recorder";

const RecordView = () => {
  const { status, startRecording, stopRecording, mediaBlobUrl } =
    useReactMediaRecorder({ video: false });

  return (
    <div className="recordView">
      <p>{status}</p>
      <video src={mediaBlobUrl} controls autoPlay loop />
      <div className="recordViewButtons">
        <button onClick={startRecording}>Start Recording</button>
        <button onClick={stopRecording}>Stop Recording</button>
        <button>Convert To Text</button>
      </div>
    </div>
  );
};

export default RecordView;
