/* groovylint-disable DuplicateStringLiteral, NestedBlockDepth */
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
                println("Git commit from checkout is ${env.GIT_COMMIT}")
            }
            stage('Install dependencies') {
                sh 'python3 -m pip install --upgrade pip'
                sh 'python3 -m pip install -r requirements.txt'
            }
            withEnv(["PYTHONPATH=$WORKSPACE/modules/"]) {
                stage('Run tests') {
                    try {
                        sh 'pytest --html=report.html'
                    }
                    catch (Exception ex) {
                        unstable("Test stage exited with exception $ex")
                    }
                }
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