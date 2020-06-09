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
    fetch('/results')
 
    .then(this.updateCropList);
  }

  componentDidMount() {
    this.getCropList();
  }

  render() {
    // const recommendedCropList = [];

    // for (const crop of this.state.cropList) {
    // recommendedCropList.push(
    //   <CropList
    //   key={this.state.cropList}
    //   cropList={this.state.cropList}
    //   />
    // );
  // }

    return ({cropList}
    );
  }
}


ReactDOM.render(
  <GetCropList />,
  document.getElementById('app')
);
