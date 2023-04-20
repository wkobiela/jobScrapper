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
    agent none
    stages {
        stage('Get changeset') {
            Map scmVars = checkout(scm)
            println(scmVars)
        }
        stage('Run CI') {
            steps {
                script {
                        // parallel parallelStages
                    }
            }
        }
    }
}