from controllers import IssueController, OrganisationController
from common.config import AppConfig
from connectors.github import GitHubConnector

import parsers

import argparse, logging, sys

logging.basicConfig(filename='log.log',level=logging.DEBUG)

cfg = AppConfig()
ghc = GitHubConnector(cfg.get_api_key(), cfg.get_repo(), cfg.get_organisation())
issue_ctrl = IssueController(ghc)
org_ctrl = OrganisationController(ghc)

def setup_argparse():
    """Sets up argparse"""
    parser = argparse.ArgumentParser(description='useful command line tools for GitHub')
    subparsers = parser.add_subparsers(dest='group', help='GitHub component in question')
    subparsers.required = True
    issue_ctrl.setup_argparse(subparsers)
    org_ctrl.setup_argparse(subparsers)
    return parser

if __name__ == '__main__':
    logging.info('Kena Arrowed - GitHub CLI tools: Started!')
    parser = setup_argparse()
    args = parser.parse_args()

    args.func(args)
