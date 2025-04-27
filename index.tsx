import { useState, FormEvent } from "react";
import axios from "axios";

export default function Home() {
  const [query, setQuery] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    if (!query.trim()) return;
    setLoading(true);
    try {
      const res = await axios.post("/api/v1/submit-query", { query });
      if (res.data && res.data.response) {
        setResponse(res.data.response);
      } else {
        setResponse("No response from model.");
      }
    } catch (error) {
      console.error(error);
      setResponse("Error fetching response.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen p-8 bg-white">
      <h1 className="text-3xl font-bold mb-8">Dynamic AI Router</h1>
      <form onSubmit={handleSubmit} className="w-full max-w-xl">
        <input
          type="text"
          className="w-full p-4 border border-gray-300 rounded-md mb-4 focus:outline-none focus:border-blue-500"
          placeholder="Ask anything..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />
        <button
          type="submit"
          className="w-full p-4 bg-blue-600 text-white rounded-md hover:bg-blue-700 transition"
          disabled={loading}
        >
          {loading ? "Thinking..." : "Submit"}
        </button>
      </form>
      {response && (
        <div className="w-full max-w-xl mt-8 p-4 border rounded-md bg-gray-50">
          <p className="text-gray-700 whitespace-pre-wrap">{response}</p>
        </div>
      )}
    </div>
  );
}
