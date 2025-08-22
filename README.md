# Tempe High School Timetable Kiosk

A production-ready web application for displaying daily timetables and bell times for Tempe High School. The application integrates with Sentral and LISS APIs to provide real-time scheduling information in an easy-to-read kiosk format.

## 🌟 Features

- **Real-time Timetable Display**: Automatically loads and displays current day's schedule
- **Bell Times Integration**: Shows period start/end times with visual indicators
- **Multi-source Data Loading**: Primary API sources with XML fallback for reliability
- **Responsive Design**: Optimized for both desktop kiosks and mobile devices
- **Debug Mode**: Comprehensive logging and troubleshooting capabilities
- **Performance Optimized**: 29x faster LISS data loading using bulk API operations

## 🚀 Live Demo

Visit the live application: [Tempe HS Timetable Kiosk](https://your-github-username.github.io/Tempe_HS_Timetable_Kiosk/)

## 📋 Quick Start

### For End Users (Kiosk Display)

Simply open `index.html` in any modern web browser. The application will automatically:

1. Load current day's timetable data
2. Display bell times and period information
3. Update throughout the day with current period highlighting

### For Administrators (Data Updates)

1. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

2. **Configure API Access**:

   - Copy configuration templates from `docs/` folder
   - Update `sentral_config.json` with your Sentral API credentials
   - Modify `config.json` for data source preferences

3. **Generate Fresh Data**:

   ```bash
   # Generate bell times
   python generate_bell_times.py

   # Generate LISS timetable data (optimized - 0.9s runtime)
   python generate_liss_info.py

   # Generate calendar data
   python generate_calendar.py
   ```

## � Project Structure

```
/
├── index.html              # Main kiosk application
├── config.json             # Application configuration
├── requirements.txt        # Python dependencies
├── sentral_config.json     # API credentials (configure this)
├── generate_liss_info.py   # LISS data generator (optimized)
├── generate_bell_times.py     # Bell times generator
├── generate_calendar.py       # Calendar generator
├── sentral_rest_client.py  # API client library
├── docs/                   # Documentation and guides
│   ├── README.md           # Detailed setup instructions
│   ├── CONFIGURATION.md    # Configuration guide
│   ├── LISS_README.md      # LISS integration guide
│   └── *.pdf              # API documentation
└── dev/                    # Development tools (tests, utilities)
```

## ⚡ Performance Features

- **Optimized LISS Loading**: Reduced from 26+ seconds to 0.9 seconds using Sentral API bulk operations
- **Smart Caching**: JSON data with XML fallback ensures fast loading with reliability
- **Minimal Dependencies**: Lightweight Python requirements for quick deployment
- **GitHub Pages Ready**: Static assets optimized for CDN delivery

## 🔧 Configuration

The application supports multiple configuration modes:

### Production Mode (Recommended)

- Uses optimized API calls for real-time data
- Automatic fallback to cached XML files
- Comprehensive error handling and logging

### Development Mode

- Enhanced debugging output
- Test data validation
- Performance monitoring

See `docs/CONFIGURATION.md` for detailed setup instructions.

## 📖 Documentation

- **[Setup Guide](docs/README.md)** - Complete installation and configuration
- **[Configuration Reference](docs/CONFIGURATION.md)** - All configuration options
- **[LISS Integration](docs/LISS_README.md)** - LISS-specific setup and optimization
- **[API Documentation](docs/)** - Sentral API guides and references

## �️ Development

Development tools and test scripts are located in the `dev/` folder:

```bash
# Run API tests
python dev/test_sentral_debug.py

# Verify endpoints
python dev/test_correct_endpoints.py

# Development utilities
python dev/discover_api_structure.py
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📞 Support

For questions about setup or configuration:

- Check the [documentation](docs/README.md)
- Review [configuration examples](docs/CONFIGURATION.md)
- Examine [API integration guides](docs/LISS_README.md)

## � About Tempe High School

This application was developed to provide efficient timetable display solutions for Tempe High School's digital kiosk systems, integrating with existing Sentral and LISS infrastructure for seamless operation.

```

```
