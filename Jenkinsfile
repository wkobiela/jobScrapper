/* groovylint-disable NestedBlockDepth */
Map parallelStages = [:]
pythonsArray = ['3.8', '3.9', '3.10', '3.11']
testStage = 'jobScrapperCI/run_tests'
runStage = 'jobScrapperCI/run_scrapper'

def generateStage(String job, String url, String commit, String python) {
    String stageName = job.replace('jobScrapperCI/', '')
    return {
        stage("Stage: ${stageName}_python${python}") {
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
                echo "Get changeset stage"
                echo "BEFORE SCMVARS ${env.GIT_COMMIT}"
                echo "BEFORE SCMVARS ${env.GIT_URL}"
                echo "BEFORE SCMVARS ${env.GIT_AUTHOR_NAME}"
                script {
                    // Map scmVars = checkout(scm)
                    // String url = scmVars.GIT_URL
                    // String commit = scmVars.GIT_COMMIT
                    // String author = scmVars.GIT_AUTHOR_NAME
                    pythonsArray.each { py ->
                        parallelStages.put("${runStage}_python${py}",
                                            generateStage(runStage, env.GIT_URL, env.GIT_COMMIT, py))
                        parallelStages.put("${testStage}_python${py}",
                                            generateStage(testStage, env.GIT_URL, env.GIT_COMMIT, py))
                    }
                }
                // buildDescription "Commit: ${commit}, Job: ${url}, Author: ${author}"
            }
        }
        stage('Run CI') {
            agent none
            steps {
                echo "Run CI stage"
                script {
                    parallel parallelStages
                    }
            }
        }
    }
}
