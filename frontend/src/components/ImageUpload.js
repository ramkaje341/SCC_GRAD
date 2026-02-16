// components/ImageUpload.js
import React, { useState } from "react";
import axios from "axios";

const ImageUpload = ({ onPrediction }) => {
  const [selectedImage, setSelectedImage] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleImageChange = (event) => {
    setSelectedImage(event.target.files[0]);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    if (!selectedImage) {
      setError("Please select an image.");
      return;
    }

    setLoading(true);
    setError("");

    const formData = new FormData();
    formData.append("image", selectedImage);

    try {
      const response = await axios.post("http://localhost:5000/predict", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });

      // Assuming the backend returns a grade in the response
      const predictedGrade = response.data.grade;
      onPrediction(predictedGrade);
    } catch (error) {
      setError("Error uploading image.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="image-upload">
      <form onSubmit={handleSubmit}>
        <input type="file" onChange={handleImageChange} />
        <button type="submit" disabled={loading}>
          {loading ? "Processing..." : "Upload Image"}
        </button>
      </form>
      {error && <p className="error">{error}</p>}
    </div>
  );
};

export default ImageUpload;
