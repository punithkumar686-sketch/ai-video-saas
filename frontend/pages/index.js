import { useState } from "react";
import axios from "axios";

export default function Home() {
  const [topic, setTopic] = useState("");
  const [video, setVideo] = useState("");

  const generate = async () => {
    const res = await axios.post("http://localhost:8000/api/generate", {
      topic
    });

    setVideo(res.data.video);
  };

  return (
    <div style={{ padding: 40 }}>
      <h1>AI Viral Video SaaS</h1>

      <input
        placeholder="Enter topic"
        onChange={(e) => setTopic(e.target.value)}
        style={{ padding: 10, width: 300 }}
      />

      <button onClick={generate} style={{ marginLeft: 10 }}>
        Generate
      </button>

      {video && (
        <video width="300" controls>
          <source src={video} />
        </video>
      )}
    </div>
  );
}
