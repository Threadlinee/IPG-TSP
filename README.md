# 🔐 IP Geolocation & Threat Detection Tool (Python)
A powerful python tool for tracking IP addresses, obtaining geolocation data, and analyzing potential threats like VPNs, TOR usage, and bots. Ideal for network security enthusiasts and privacy-conscious users.

# ✨ Features

🌍 Tracks IP geolocation info (city, country, latitude, longitude, ISP)

🔎 Detects VPN, TOR, and bot activities using real-time threat analysis

💾 Saves geo-data and threat info to your desktop for later review

🌐 Supports scanning both your own IP and any provided IP address

💡 Displays relevant information including timezone and currency

✅ Utilizes ipgeolocation.io and ip-api APIs for accurate results

# ⚙️ How It Works
This tool makes use of two key APIs to gather IP data and detect threats:

Geo-Data: Get location, ISP, timezone, and currency information for any IP address.

Threat Detection: Check for VPN, TOR, and bot activity to assess IP security.

# 💻 How to Run
# 🪟 Windows

Make sure .NET SDK is installed.

Open CMD or PowerShell in the folder containing the .cs file.

Build and run:

dotnet new console -o IPGeolocationApp  
cd IPGeolocationApp  
# Replace default Program.cs  
copy ..\Program.cs .\Program.cs  
dotnet build  
After building, run the .exe directly:

cd bin\Debug\net8.0  
IPGeolocationThreatScanner.exe
🐧 Linux

Install .NET SDK:

sudo apt update  
sudo apt install dotnet-sdk-8.0  
In terminal:

dotnet new console -o IPGeolocationApp  
cd IPGeolocationApp  
mv ../Program.cs ./Program.cs  
dotnet run  
Or, build and run the output manually:

dotnet build  
cd bin/Debug/net8.0  
./IPGeolocationThreatScanner  
# 🧪 Example Usage
Enter IP address: 8.8.8.8
# ✅ Geo-data fetched and threat analysis completed:
IP: 8.8.8.8
Location: Mountain View, California, USA
VPN: Not Detected
TOR: Not Detected
Bot Status: Clean

# ⚠️ Disclaimer
This tool is for informational purposes and basic threat analysis. Results are based on free APIs and may not be 100% accurate for all IP addresses.

# 📄 License
Open-source under the MIT License.

👤 Author
Made by @Threadlinee with ❤️

