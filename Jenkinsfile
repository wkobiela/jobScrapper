podTemplate(
    containers: [
    containerTemplate(
        name: 'python',
        image: 'python:latest',
        command: 'sleep',
        args: '99d',
        resourceRequestCpu: '1',
        resourceLimitCpu: '2',
        resourceRequestMemory: '2Gi',
        resourceLimitMemory: '4Gi',
        )],
        nodeSelector: 'bigger=true'
        ) {

    node(POD_LABEL) {
        container('python') {
            stage('Clone') {
                checkout scm
            }
            stage('Install dependencies') {
                sh 'python3 -m pip install -r requirements.txt'
            }
            stage('Setup env') {
                sh "export PYTHONPATH='$WORKSPACE/modules/'"
            }
            stage('Run tests') {
                sh 'pytest --html=report.html'
            }
            stage('Publish report') {
                publishHTML(target: [
                        allowMissing: true,
                        alwaysLinkToLastBuild: false,
                        keepAll: false,
                        reportDir: "$WORKSPACE",
                        reportFiles: '*.html',
                        reportName: 'Pytest Report'
                ])
            }
        }
    }
}