<h1>SDES (Simplified Data Encryption Standard)</h1>
<span class="badge">MIT License</span>

<h2>Overview</h2>
<p>SDES is a simplified version of the Data Encryption Standard (DES) designed to illustrate the core concepts of block cipher algorithms. This implementation focuses on demonstrating the fundamental principles of encryption and decryption using SDES, making it an excellent resource for educational purposes.</p>

<h2>Features</h2>
<ul>
    <li><strong>Encryption and Decryption:</strong> Implements the basic encryption and decryption functionalities of the SDES algorithm.</li>
    <li><strong>Key Generation:</strong> Supports key generation using a 10-bit key.</li>
    <li><strong>Permutations and Substitutions:</strong> Includes detailed permutations and substitutions operations to show how SDES transforms data.</li>
</ul>

<h2>Getting Started</h2>
<p>To use this project, follow these steps:</p>

<ol>
    <li><strong>Clone the Repository:</strong></li>
    <pre><code>git clone https://github.com/jayypatel18/SDES.git
cd SDES</code></pre>
    <li><strong>Build the Project:</strong></li>
    <p>Follow the instructions specific to your development environment. For example, you may need to use <code>make</code> or another build tool if applicable.</p>
    <li><strong>Run the Example:</strong></li>
    <p>After building the project, you can run the example to see SDES in action. Make sure to provide the necessary input parameters (like the key and plaintext) as specified in the documentation.</p>
</ol>

<h2>Usage</h2>
<p>Here's a brief overview of how to use the SDES implementation:</p>

<pre><code>from sdes import SDES

# Initialize SDES with a 10-bit key
key = "1010000010"
sdes = SDES(key)

# Encrypt plaintext
plaintext = "11001100"
ciphertext = sdes.encrypt(plaintext)
print(f"Ciphertext: {ciphertext}")

# Decrypt ciphertext
decrypted_text = sdes.decrypt(ciphertext)
print(f"Decrypted Text: {decrypted_text}")</code></pre>

<h2>Contributing</h2>
<p>Contributions are welcome! If you have suggestions or improvements, please open an issue or submit a pull request.</p>

<ol>
    <li><strong>Fork the Repository</strong></li>
    <li><strong>Create a Feature Branch</strong></li>
    <li><strong>Commit Your Changes</strong></li>
    <li><strong>Push to the Branch</strong></li>
    <li><strong>Open a Pull Request</strong></li>
</ol>

<h2>License</h2>
<p>This project is licensed under the MIT License. See the <a href="LICENSE">LICENSE</a> file for details.</p>

<h2>Acknowledgments</h2>
<ul>
    <li><a href="https://en.wikipedia.org/wiki/Simplified_Data_Encryption_Standard">SDES Algorithm</a> - Reference for the SDES algorithm.</li>
</ul>

<h2>Contact</h2>
<p>For any questions or support, please contact <a href="https://github.com/jayypatel18">jayypatel18</a>.</p>

</body>
</html>