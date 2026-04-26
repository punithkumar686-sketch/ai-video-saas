import { useState } from "react";

function App() {
  const [text, setText] = useState("");
  const [video, setVideo] = useState("");

  const generateVideo = async () => {
    const res = await fetch("http://localhost:8001/generate-video?text=" + text, {
      method: "POST"
    });

    const data = await res.json();
    setVideo(data.video_path);
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>AI Video Generator</h1>

      <input
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Enter text"
      />

      <button onClick={generateVideo}>
        Generate Video
      </button>

      {video && (
        <div>
          <h3>Output:</h3>
          <p>{video}</p>
        </div>
      )}
    </div>
  );
}

export default App;
