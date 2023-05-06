/* groovylint-disable NestedBlockDepth */
Map parallelStages = [:]
pythonsArray = ['3.7', '3.8', '3.9', '3.10', '3.11']
testStage = 'jobScrapperCI/run_scrapper'
runStage = 'jobScrapperCI/run_tests'

def generateStage(String job, String url, String commit, String python) {
    String stageName = job.replace('jobScrapperCI/', '')
    return {
        stage("Stage: ${stageName}") {
            build job: "${job}",
            parameters: [string(name: 'Repo_url', value: "${url}"),
                        string(name: 'Commit', value: "${commit}"),
                        string(name: 'Python', value: "${python}"),
                        booleanParam(name: 'propagateStatus', value: true)
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
                    pythonsArray.each { python ->
                        parallelStages.put("${runStage}_${python}", generateStage(runStage, url, commit, python))
                    }
                    parallelStages.put(testStage, generateStage(testStage, url, commit, '3'))
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