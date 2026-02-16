// App.js
import React, { useState } from "react";
import ImageUpload from "./components/ImageUpload";
import PredictionResult from "./components/PredictionResult";
import "./App.css";

function App() {
  const [prediction, setPrediction] = useState(null);

  const handlePrediction = (predictedGrade) => {
    setPrediction(predictedGrade);
  };

  return (
    <div className="App">
      <h1>Squamous Cell Carcinoma Grading</h1>
      <ImageUpload onPrediction={handlePrediction} />
      {prediction && <PredictionResult grade={prediction} />}
    </div>
  );
}

export default App;
