/* groovylint-disable NestedBlockDepth */
Map parallelStages = [:]
jobsArray = ['jobScrapperCI/run_tests']
// , 'jobScrapperCI/install_requirements'
def generateStage(job, url, commit) {
    String stageName = job.replace('jobScrapperCI/', '')
    return {
        stage("Stage: ${stageName}") {
            build job: "${job}",
            parameters: [string(name: 'Repo_url', value: "${url}"),
                        string(name: 'Commit', value: "${commit}"),
                        ],
            wait: true
        }
    }
}

pipeline {
    agent none
    stages {
        stage('Get changeset') {
            agent any
            steps {
                script {
                    Map scmVars = checkout(scm)
                    String url = scmVars.GIT_URL
                    String commit = scmVars.GIT_COMMIT
                    jobsArray.each { job ->
                        parallelStages.put("${job}", generateStage(job, url, commit))
                    }
                }
            }
        }
        stage('Run CI') {
            agent none
            steps {
                script {
                    parallel parallelStages
                    }
            }
        }
    }
}