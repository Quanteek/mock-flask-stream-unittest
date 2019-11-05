import json

from flask import Flask, Response


def create_app(config=None):
    app = Flask(__name__)

    @app.route("/")
    def index():
        return {"message": "I am a mock server with streaming capabilities."}

    @app.route("/object_list")
    def object_list():
        object_metadata_list = [{"id": "0", "version": "0"},
                                {"id": "1", "version": "0"},
                                {"id": "2", "version": "0"},
                                {"id": "3", "version": "0"},
                                {"id": "4", "version": "0"}]

        def events():
            for object_metadata in object_metadata_list:
                yield "{}\n".format(json.dumps(object_metadata))

        return Response(events(), content_type="text/event-stream")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)
