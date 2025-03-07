import React, { useState } from 'react';
import FileUpload from './components/FileUpload';

function App() {
    const [suggestions, setSuggestions] = useState([]);

    return (
        <div>
            <h1>Graph Suggestion App</h1>
            <FileUpload onFileUpload={setSuggestions} />
            <pre>{JSON.stringify(suggestions, null, 2)}</pre>
        </div>
    );
}

export default App;
