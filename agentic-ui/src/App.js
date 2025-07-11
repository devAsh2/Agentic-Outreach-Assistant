import {useState } from 'react';
import axios from 'axios';

function App() {
  // defining the states i need here for the generate email UI
  //companyurl//productdescription//generatedEmail//error
  //loading
  const [companyUrl, setCompanyUrl] = useState('');
  const [productDescription, setProductDescription] = useState('');
  const [generatedEmail, setGeneratedEmail] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  const [isPressed, setIsPressed] = useState(false);

  //handle submit logic
  const handleSubmit = async(e) =>{
    e.preventDefault();
    setLoading(true);
    setError('');
    setGeneratedEmail('');
    
    try{
      const response = await axios.post("http://localhost:8000/api/generate/", {
        company_url: companyUrl,
        product_description: productDescription,
      });

      setGeneratedEmail(response.data.email);
    }
    catch(err){
      setError('Failed to generate email. Please try again.');
      console.error(err);
    }
    finally{
      setLoading(false);
    }
  }
  
  return (
    <div>
      <h1>Agentic Outreach Assistant</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Enter company url"
          onChange={(e) => setCompanyUrl(e.target.value)}
          value={companyUrl}
          style={{width: "40%"}}
        />
        <br />
        <input
          type="text"
          placeholder="Describe your product in one sentence"
          onChange={(e) => setProductDescription(e.target.value)}
          value={productDescription}
          style={{ width: "70%", marginTop: "10px" }}
        />
        <br />
        <button
          onMouseDown={() => setIsPressed(true)}
          onMouseUp={() => setIsPressed(false)}
          onMouseLeave={() => setIsPressed(false)}
          type="submit"
          disabled={loading}
          style={{
            marginTop: "10px",
            backgroundColor: isPressed ? "#B30041" : "pink",
            color: "black",
            padding: "10px",
            cursor: "pointer",
            borderRadius: "4px",
            transition: "background-color 0.2s ease",
          }}>
          {loading ? "Generating..." : "Generate Email"}
        </button>
      </form>

      {error && <p style={{ color: "red" }}>{error}</p>}

      {generatedEmail && (
        <div>
          <h2>Generated Email:</h2>
          <pre>{generatedEmail}</pre>
        </div>
      )}
    </div>
  );
}

export default App;
