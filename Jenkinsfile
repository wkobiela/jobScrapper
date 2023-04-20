Map parallelStages = [:]
jobsArray = ['jobScrapperCI/run_tests', 'jobScrapperCI/install_requirements']

def generateStage(job) {
    return {
        stage("Stage: ${job}") {
            build job: "${job}",
            wait: true
        }
    }
}

jobsArray.each { job ->
    parallelStages.put("${job}", generateStage(job))
}

pipeline {
    stages {
        stage('Get changeset') {
            agent any
            steps {
                Map scmVars = checkout(scm)
                println(scmVars)
            }
        }
        stage('Run CI') {
            agent none
            steps {
                script {
                        // parallel parallelStages
                    }
            }
        }
    }
}