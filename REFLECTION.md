
Development & Deployment Reflection
Key Experiences & Architecture
Building this project highlighted the benefits of separating database concerns (SQLAlchemy ORM models and CRUD methods) from HTTP API routes (FastAPI). The front-end communicates asynchronously via standard fetch calls, ensuring that database updates immediately reflect in the dynamic table without requiring full page reloads.

Challenges & Solutions
Division by Zero & Edge Cases: Handled both client-side (preventing form submissions with operand2 == 0 for division) and server-side (raising an HTTP 400 Exception) to prevent application errors.

CI/CD Pipeline Setup: Configuring the GitHub Actions runner to launch the backend web server in the background prior to triggering Playwright E2E tests required using background process management (python app.py &) and sleep buffers to allow database initialization.

Conclusion
The project successfully achieves full coverage across BREAD functionality, robust schema validations, E2E test execution, and continuous delivery via Docker containerization.
