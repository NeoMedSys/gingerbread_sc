import React, { useEffect } from 'react';

function App() {
  useEffect(() => {
    // Redirect to the desired URL when the component mounts
    window.location.href = 'https://neomedsys.github.io/gingerbread_sc/';
  }, []);

  // This component doesn't render anything since it immediately redirects.
  return null;
}

export default App;