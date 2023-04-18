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
            stage('Run tests') {
                sh 'ls -al'
                sh 'pwd'
                sh 'pytest'
            }
        }
    }
}