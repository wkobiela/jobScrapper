statusName = "Jenkins CI"

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
            try {
                stage('Clone') {
                    sh 'ls -l'
                }
            } catch (Exception e) {
                error "Exception message: $e"
                currentBuild.result = 'FAILURE'
            } finally {
                if (currentBuild.result == 'FAILURE' || currentBuild.result == 'UNSTABLE' || currentBuild.result == 'ABORTED') {
                    statusUpdate('failure')
                } else {
                    statusUpdate('success')
                }
            }
        }
    }
}

def statusUpdate(status) {
    withCredentials([string(credentialsId: 'github_token', variable: 'TOKEN')]) {
        cmd = """curl "https://api.github.com/repos/wkobiela/jobScrapper/statuses/$GIT_COMMIT" \
        -H "Content-Type: application/json" \
        -H "Authorization: token """ + TOKEN + """\" \
        -X POST \
        -d "{\\"state\\": \\"${status}\\",\\"context\\": \\"${statusName}\\", \
        \\"description\\": \\"Jenkins\\", \\"target_url\\": \\"${env.BUILD_URL}\\"}\""""
        sh label: 'Update Github actions status', script: cmd
    }
}