pipeline {
    agent any

    environment {
        // Enforces headless execution so Chrome doesn't crash trying to open a UI window
        MOZ_HEADLESS = '1'
    }

    stages {
        stage('Checkout Code') {
            steps {
                // Pulls code from your GitHub repository automatically
                checkout scm
            }
        }

        stage('Setup Environment') {
            steps {
                // Create a Python virtual environment and install requirements
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install pytest selenium pytest-html
                '''
            }
        }

        stage('Run Selenium Tests') {
            steps {
                // Execute tests and generate an HTML report
                sh '''
                    . venv/bin/activate
                    pytest test_*.py --html=report.html --self-contained-html || true
                '''
            }
        }
    }

    post {
        always {
            // Archives and publishes the test report in Jenkins
            publishHTML([
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: '.',
                reportFiles: 'report.html',
                reportName: 'Selenium Test Report'
            ])
        }
    }
}
