class CropList extends React.Component {

  render() {
    return (
      <div>
        <p>'Test'</p>
        <p>{this.props.cropList}</p>
      </div>
      );
  }
}

class GetCropList extends React.Component {
  constructor() {
    super();

    this.state = { cropList: []};
    this.updateCropList = this.updateCropList.bind(this);
  }

  updateCropList(response) {
      const cropList = response.cropList

      this.setState({ cropList: cropList});
  }

  getCropList() {
    //Note I can't get the below to work because not getting a jsonified dictionary!!!
    fetch('/results')
    .then(response => response.json())
    .then(this.updateCards);
  }

  componentDidMount() {
    this.getCropList();
    }

  render() {
    const recommendedCropList = [];

    for (const crop of this.state.cropList) {
      recommendedCropList.push(
        <CropList
          key={crop.name}
          name={crop.name}
        />
      );
    }

    return (
      <div>{recommendedCropList}</div>
    );
  }
}


ReactDOM.render(
  <GetCropList />,
  document.getElementById('app')
);
