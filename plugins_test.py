import unittest
from plugins import getPlugins
import os
import platform

OS = os.environ.get("OS", platform.system().lower())


class TestGetPlugins(unittest.TestCase):
    def test_get_plugin_with_version(self):
        os.environ[
            "GRAFANA_PLUGINS"
        ] = "grafana-clock-panel:1.0.1,grafana-simple-json-datasource:1.3.5"
        actual = getPlugins()
        expected = [
            (
                "https://grafana.com/api/plugins/grafana-clock-panel/versions/1.0.1/download?os="
                + OS
                + "&arch=x86_64",
                "/tmp/grafana-clock-panel_1.0.1.zip",
            ),
            (
                "https://grafana.com/api/plugins/grafana-simple-json-datasource/versions/1.3.5/download?os="
                + OS
                + "&arch=x86_64",
                "/tmp/grafana-simple-json-datasource_1.3.5.zip",
            ),
        ]
        self.assertEqual(actual, expected)

    def test_get_plugin_without_version(self):
        os.environ[
            "GRAFANA_PLUGINS"
        ] = "grafana-clock-panel:1.0.1,grafana-simple-json-datasource"
        actual = getPlugins()
        expected = [
            (
                "https://grafana.com/api/plugins/grafana-clock-panel/versions/1.0.1/download?os="
                + OS
                + "&arch=x86_64",
                "/tmp/grafana-clock-panel_1.0.1.zip",
            ),
            (
                "https://grafana.com/api/plugins/grafana-simple-json-datasource/versions/latest/download?os="
                + OS
                + "&arch=x86_64",
                "/tmp/grafana-simple-json-datasource_latest.zip",
            ),
        ]
        self.assertEqual(actual, expected)

    def test_get_plugin_without_multiple(self):
        os.environ["GRAFANA_PLUGINS"] = "grafana-clock-panel:1.0.1"
        actual = getPlugins()
        expected = [
            (
                "https://grafana.com/api/plugins/grafana-clock-panel/versions/1.0.1/download?os="
                + OS
                + "&arch=x86_64",
                "/tmp/grafana-clock-panel_1.0.1.zip",
            ),
        ]
        self.assertEqual(actual, expected)

    def test_get_plugin_withurl(self):
        os.environ[
            "GRAFANA_PLUGINS"
        ] = "url:https://grafana.com/api/plugins/grafana-clock-panel"
        actual = getPlugins()
        expected = [
            (
                "https://grafana.com/api/plugins/grafana-clock-panel",
                "/tmp/grafana-clock-panel.zip",
            ),
        ]

        self.assertEqual(actual, expected)

    def test_get_plugin_withurl_multiple(self):
        os.environ[
            "GRAFANA_PLUGINS"
        ] = "url:https://grafana.com/api/plugins/grafana-clock-panel,grafana-clock-panel:1.0.1"
        actual = getPlugins()
        expected = [
            (
                "https://grafana.com/api/plugins/grafana-clock-panel",
                "/tmp/grafana-clock-panel.zip",
            ),
            (
                "https://grafana.com/api/plugins/grafana-clock-panel/versions/1.0.1/download?os="
                + OS
                + "&arch=x86_64",
                "/tmp/grafana-clock-panel_1.0.1.zip",
            ),
        ]

        self.assertEqual(actual, expected)

    def test_get_plugin_withurl_multiple_similar(self):
        os.environ[
            "GRAFANA_PLUGINS"
        ] = "url:https://grafana.com/api/plugins/grafana-clock-panel,url:https://grafana.com/api/plugins/grafana-simple-json-datasource"
        actual = getPlugins()
        expected = [
            (
                "https://grafana.com/api/plugins/grafana-clock-panel",
                "/tmp/grafana-clock-panel.zip",
            ),
            (
                "https://grafana.com/api/plugins/grafana-simple-json-datasource",
                "/tmp/grafana-simple-json-datasource.zip",
            ),
        ]

        self.assertEqual(actual, expected)

    def test_get_plugin_withurl_multiple_withoutversion(self):
        os.environ[
            "GRAFANA_PLUGINS"
        ] = "url:https://grafana.com/api/plugins/grafana-clock-panel,grafana-clock-panel"
        actual = getPlugins()
        expected = [
            (
                "https://grafana.com/api/plugins/grafana-clock-panel",
                "/tmp/grafana-clock-panel.zip",
            ),
            (
                "https://grafana.com/api/plugins/grafana-clock-panel/versions/latest/download?os="
                + OS
                + "&arch=x86_64",
                "/tmp/grafana-clock-panel_latest.zip",
            ),
        ]

        self.assertEqual(actual, expected)

    def test_get_plugin_withurl_multiple_withoutversion_reverse(self):
        os.environ[
            "GRAFANA_PLUGINS"
        ] = "grafana-clock-panel,url:https://grafana.com/api/plugins/grafana-clock-panel"
        actual = getPlugins()
        expected = [
            (
                "https://grafana.com/api/plugins/grafana-clock-panel/versions/latest/download?os="
                + OS
                + "&arch=x86_64",
                "/tmp/grafana-clock-panel_latest.zip",
            ),
            (
                "https://grafana.com/api/plugins/grafana-clock-panel",
                "/tmp/grafana-clock-panel.zip",
            ),
        ]

        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
