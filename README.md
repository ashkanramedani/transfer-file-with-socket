<h1>File Transfer with Socket</h1>
<p>This project provides a simple file transfer mechanism using Python sockets. It includes two main scripts:</p>
<ul>
  <li><strong>Sender</strong>: Sends a large file to the server in chunks.</li>
  <li><strong>Receiver</strong>: Receives the file on the server and reassembles it.</li>
</ul>
<h3>Requirements</h3>
<p>Make sure Python is installed on both client and server machines. Install the required packages with:</p>
<pre><code>pip install -r requirements.txt
</code></pre>
<p>The required packages are:</p>
<ul>
  <li><code>tqdm</code> for progress display.</li>
</ul>
<h3>Setup and Usage</h3>
<h4>Step 1: Set up the Receiver on the Server</h4>
<ol>
  <li>
    <p>Edit the <code>receiver.py</code> script to set the correct <code>SAVE_PATH</code>, <code>SERVER_IP</code>, and <code>SERVER_PORT</code> values.</p>
    <ul>
      <li><strong>SAVE_PATH</strong>: Directory where the file will be saved.</li>
      <li><strong>SERVER_IP</strong>: Set to <code>0.0.0.0</code> to listen on all network interfaces.</li>
      <li><strong>SERVER_PORT</strong>: The port the server listens on.</li>
    </ul>
  </li>
  <li>
    <p>Run the receiver script:</p>
    <div>
      <div>&nbsp;</div>
      <div dir="ltr"><code>python receiver.py </code></div>
    </div>
    <p>The server is now ready to receive files.</p>
  </li>
</ol>
<h4>Step 2: Configure and Run the Sender</h4>
<ol>
  <li>
    <p>Edit the <code>sender.py</code> script to set <code>SERVER_IP</code>, <code>SERVER_PORT</code>, and <code>FILE_PATH</code> values.</p>
    <ul>
      <li><strong>SERVER_IP</strong>: Server's IP address.</li>
      <li><strong>SERVER_PORT</strong>: The port the server listens on.</li>
      <li><strong>FILE_PATH</strong>: Path to the file you want to transfer.</li>
    </ul>
  </li>
  <li>
    <p>Run the sender script:</p>
    <div>
      <div>&nbsp;</div>
      <div dir="ltr"><code>python sender.py </code></div>
    </div>
    <p>The file will now be sent in chunks to the server.</p>
  </li>
</ol>
<h3>Notes</h3>
<ul>
  <li>Ensure that both client and server are on the same network or have internet access to each other.</li>
  <li>Adjust the <code>CHUNK_SIZE</code> and <code>NUM_THREADS</code> in both scripts if necessary to optimize transfer speed.</li>
</ul>
