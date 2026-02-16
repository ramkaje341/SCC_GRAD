// components/PredictionResult.js
import React from "react";

const PredictionResult = ({ grade }) => {
  return (
    <div className="prediction-result">
      <h2>Predicted Grade: {grade}</h2>
    </div>
  );
};

export default PredictionResult;
